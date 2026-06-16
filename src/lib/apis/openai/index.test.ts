import { afterEach, describe, expect, it, vi } from 'vitest';

import { verifyOpenAIConnection } from './index';

describe('verifyOpenAIConnection', () => {
	afterEach(() => {
		vi.restoreAllMocks();
	});

	it('surfaces provider error messages returned without an error wrapper', async () => {
		vi.stubGlobal(
			'fetch',
			vi.fn().mockResolvedValue({
				ok: false,
				json: vi.fn().mockResolvedValue({
					code: 'API_KEY_REQUIRED',
					message: 'API key is required in Authorization header'
				})
			})
		);

		await expect(
			verifyOpenAIConnection('webui-token', {
				url: 'https://api.example.com/v1',
				key: '',
				config: { auth_type: 'bearer' }
			})
		).rejects.toBe('OpenAI: API key is required in Authorization header');
	});
});
