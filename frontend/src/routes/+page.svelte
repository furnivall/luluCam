<script>
  import VideoFeed from '$src/lib/VideoFeed.svelte';
  import AudioControls from '$src/lib/AudioControls.svelte';
  import TempHumidity from '$src/lib/TempHumidity.svelte';
</script>

<main>
  <VideoFeed />
  <AudioControls />
  <TempHumidity />
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
  }
</style>

