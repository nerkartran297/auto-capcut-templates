function importAssetsToProject(folderPath, audioPath) {
    var project = app.project;

    if (!project) {
        alert("No project is open.");
        return;
    }

    var imageFiles = [];
    var folder = new Folder(folderPath);
    if (folder.exists) {
        var files = folder.getFiles();
        for (var i = 0; i < files.length; i++) {
            if (files[i] instanceof File && /\.jpe?g$|\.png$/i.test(files[i].name)) {
                imageFiles.push(files[i]);
            }
        }
    }

    if (imageFiles.length === 0) {
        alert("No images found in the folder: " + folderPath);
        return;
    }

    var imageClips = [];
    for (var j = 0; j < imageFiles.length; j++) {
        var imageFile = new File(imageFiles[j].fsName);
        project.importFiles([imageFile.fsName], false, project.rootItem, false);
        var lastImported = project.rootItem.children[project.rootItem.children.length - 1];
        imageClips.push(lastImported);
    }

    var audioFile = new File(audioPath);
    if (audioFile.exists) {
        project.importFiles([audioFile.fsName], false, project.rootItem, false);
        var audioClip = project.rootItem.children[project.rootItem.children.length - 1];
        return { imageClips: imageClips, audioClip: audioClip };
    } else {
        alert("Audio file not found: " + audioPath);
        return;
    }
}

function createVideoSequence(sequenceName, imageClips, audioClip) {
    var sequence = app.project.createNewSequence(sequenceName, "Custom_1024x1280_30fps");

    var videoTrack = sequence.videoTracks[0];
    var audioTrack = sequence.audioTracks[0];

    var slideDuration = 0;

    var currentTime = 0;
    for (var i = 0; i < imageClips.length; i++) {
        var clip = videoTrack.insertClip(imageClips[i], currentTime);
        clip.end = clip.start + slideDuration;

        currentTime += slideDuration;
    }

    audioTrack.insertClip(audioClip, 0);

    app.enableQE();

    var qeTrack = qe.project.getActiveSequence().getVideoTrackAt(0);
    if (qeTrack) {
        var qeClip = qeTrack.getItemAt(0);
        if (qeClip) {
            var effectToAdd = qe.project.getVideoEffectByName("Crop");
            if (effectToAdd) {
                qeClip.addVideoEffect(effectToAdd);
            }
        }
    }

    return sequence;
}

function exportSequenceToMP4(sequenceName, outputPath) {
    var sequence = app.project.sequences[0]; // Use the first sequence as Premiere Pro doesn’t support sequence by name directly
    if (!sequence) {
        alert("Sequence not found.");
        return;
    }

    var presetPath = File("D:/1. Working/PSA/auto-bot/PSApreset.epr").fsName; // Adjust to your .epr preset path

    app.encoder.encodeSequence(
        sequence,
        outputPath, // Output file path
        presetPath, // Encoding preset
        1, // Export the work area
        true // Remove from queue upon completion
    );

    alert("Rendering started. Check Adobe Media Encoder for progress.");
}

var n = 1;

var qe = app.enableQE();

if (n == 0) {
    var imageFolderPath = "D:/1. Working/PSA/auto-bot/output/script_1/images";
    var audioFilePath = "D:/1. Working/PSA/auto-bot/output/script_1/audio/script_audio.mp3";
    var outputFilePath = "D:/1. Working/PSA/auto-bot/output/output.mp4";

    var assets = importAssetsToProject(imageFolderPath, audioFilePath);
    if (assets) {
        var sequenceName = "SlideVideo";
        createVideoSequence(sequenceName, assets.imageClips, assets.audioClip);
    } else {
        alert("Error occurred while importing assets.");
    }
}

if (n == 1)
    exportSequenceToMP4(sequenceName, outputFilePath);


