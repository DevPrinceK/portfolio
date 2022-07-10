var youtubeEmbedElement = document.getElementById("youtubeEmbed"),
    tag = document.createElement("script");
tag.src = "https://www.youtube.com/iframe_api";
var player, firstScriptTag = document.getElementsByTagName("script")[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
var videoId = youtubeEmbedElement.dataset.videoId,
    startSeconds = 14,
    endSeconds = 210;
onYouTubeIframeAPIReady = function() {
    player = new YT.Player("youtubeEmbed", {
        videoId: videoId,
        playerVars: {
            autoplay: 1,
            autohide: 1,
            disablekb: 1,
            controls: 0,
            showinfo: 0,
            modestbranding: 1,
            loop: 1,
            fs: 0,
            rel: 0,
            enablejsapi: 1,
            start: startSeconds,
            end: endSeconds
        },
        events: {
            onReady: function(e) {
                e.target.mute(), e.target.playVideo()
            },
            onStateChange: function(e) {
                e.data === YT.PlayerState.PLAYING && document.getElementById("youtubeEmbed").classList.add("loaded"), e.data === YT.PlayerState.ENDED && player.seekTo(startSeconds)
            }
        }
    })
};