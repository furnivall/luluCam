import { test } from 'vitest';
import { render } from '@testing-library/svelte';
import AudioControls from '../lib/audiocontrols.svelte';
import '@testing-library/jest-dom'

test('AudioControls component should render the Broadcast Audio button', () => {
  const { getByText } = render(AudioControls);
  const buttonElement = getByText('Broadcast Audio');
  expect(buttonElement).toBeInTheDocument();
});

