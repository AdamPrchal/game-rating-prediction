import "../styles/pico.min.css";
import "../styles/main.css";

export const metadata = {
  title: "Strojové učení – Predikce hodnocení videoher",
  description:
    "Projekt Strojového Učení: Předpověď Hodnocení Videoher - Tento projekt demonstruje využití metod strojového učení k předpovědi hodnocení videoher na základě různých atributů, včetně žánru, platformy a času potřebného k dokončení hry.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" data-theme="light" style={{ scrollBehavior: "smooth" }}>
      <head>
        <link
          rel="apple-touch-icon"
          sizes="180x180"
          href="/apple-touch-icon.png"
        />
        <link
          rel="icon"
          type="image/png"
          sizes="32x32"
          href="/favicon-32x32.png"
        />
        <link
          rel="icon"
          type="image/png"
          sizes="16x16"
          href="/favicon-16x16.png"
        />
        <link rel="manifest" href="/site.webmanifest" />
        <meta name="msapplication-TileColor" content="#da532c" />
        <meta name="theme-color" content="#ffffff" />
      </head>
      <body>{children}</body>
    </html>
  );
}
