const withMDX = require('@next/mdx')()

/** @type {import("next").NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  pageExtensions: ['js', 'jsx', 'mdx', 'ts', 'tsx'],

  experimental: {
    mdxRs: true
  }
};

module.exports = withMDX(nextConfig)