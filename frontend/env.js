const env = process.env.NUXT_ENV_IS;

let envApiUrl = "";
if (env === 'production') {
  envApiUrl = "https://chili-lingerie.com";
} else {
  envApiUrl = "http://localhost";
}

export const apiUrl = envApiUrl;
