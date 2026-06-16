import { describe, expect, it } from 'vitest';

import { APP_NAME } from './constants';

describe('APP_NAME', () => {
	it('uses JackAI as the built-in app name', () => {
		expect(APP_NAME).toBe('JackAI');
	});
});
