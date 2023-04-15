import { test } from 'vitest';
import { render } from '@testing-library/svelte';
import TempHumidity from 'src/lib/TempHumidity.svelte';
import '@testing-library/jest-dom'

test('TempHumidity component should render temperature and humidity elements', () => {
  const { getByText } = render(TempHumidity);
  const temperatureElement = getByText(/Temperature: -- °C/i);
  const humidityElement = getByText(/Humidity: -- %/i);
  expect(temperatureElement).toBeInTheDocument();
  expect(humidityElement).toBeInTheDocument();
});

