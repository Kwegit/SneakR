// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  
  modules: [
    '@nuxt/ui',
    '@nuxtjs/tailwindcss',
    '@nuxt/image',
    '@nuxtjs/supabase',
  ],
  supabase: {
    redirectOptions: {
      // Pour rediriger l'utilisateur si il n'est pas connecté
      login: "/Login", // Redirige vers la page de login s'il nes pas connecté ou s'il s'est logout
      callback: "/",
      exclude: [
        // Page que l'utilisateur peut visiter sans être connecté
        "/Login",
        "/Register",
        "/",
        "/index",
        "/detail/*",
        "/updatePassword",
        "/resetPassword",
      ],
    },
  },
  colorMode: {
    preference: 'light'
  }
})

