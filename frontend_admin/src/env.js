const env = process.env.VUE_APP_ENV;

let envApiUrl = '';
if (env === 'prod') {
  envApiUrl = process.env.VUE_APP_DOMAIN_PROD;
} else {
  envApiUrl = process.env.VUE_APP_DOMAIN_DEV;
}
export const apiUrl = envApiUrl;
