const { getDefaultConfig } = require('expo/metro-config');

const config = getDefaultConfig(__dirname);

// Add required extensions for TensorFlow models and storage resolution
config.resolver.assetExts.push('bin'); // For moving model weights
config.resolver.sourceExts.push('js', 'json', 'ts', 'tsx', 'cjs', 'mjs');

module.exports = config;
