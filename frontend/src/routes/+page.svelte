<script>
  import VideoFeed from '../lib/VideoFeed.svelte';
  import AudioControls from '../lib/AudioControls.svelte';
  import TempHumidity from '../lib/TempHumidity.svelte';
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
