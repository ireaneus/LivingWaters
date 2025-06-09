export const BASE = import.meta.env.PROD ? '/LivingWaters/' : '/';
export const NAV_LINKS = [
  { name: 'home', href: BASE },
  { name: 'about', href: BASE + 'about/' },
  { name: 'blog', href: BASE + 'blog/' },
];