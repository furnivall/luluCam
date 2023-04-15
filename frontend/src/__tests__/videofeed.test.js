import { test } from 'vitest';
import { render } from '@testing-library/svelte';
import VideoFeed from '../lib/VideoFeed.svelte';
import '@testing-library/jest-dom'

test('VideoFeed component should render a video element', () => {
  const { container } = render(VideoFeed);
  const videoElement = container.querySelector('video');
  expect(videoElement).toBeInTheDocument();
});

