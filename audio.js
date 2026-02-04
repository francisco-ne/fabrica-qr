const audio = document.getElementById("audio");
const playBtn = document.getElementById("playBtn");
const progress = document.getElementById("progress");

let maxEscuchado = 0;

playBtn.addEventListener("click", () => {
    if (audio.paused) {
        audio.play();
        playBtn.textContent = "⏸ Pausar";
    } else {
        audio.pause();
        playBtn.textContent = "▶ Reproducir";
    }
});

audio.addEventListener("timeupdate", () => {
    progress.max = audio.duration;
    progress.value = audio.currentTime;

    if (audio.currentTime > maxEscuchado) {
        maxEscuchado = audio.currentTime;
    }
});

progress.addEventListener("input", () => {
    if (progress.value <= maxEscuchado) {
        audio.currentTime = progress.value;
    } else {
        progress.value = maxEscuchado;
    }
});

audio.addEventListener("ended", () => {
    playBtn.textContent = "▶ Reproducir";
});
