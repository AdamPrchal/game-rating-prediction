import Uvod from "../chapters/uvod.mdx";
import ZiskaniDat from "../chapters/ziskaniDat.mdx";
import AnalyzaDat from "../chapters/analyzaDat.mdx";
import VyberModelu from "../chapters/vyberModelu.mdx";
import TrenovaniModelu from "../chapters/trenovaniModelu.mdx";
import PredzpracovaniDat from "../chapters/predzpracovaniDat.mdx";
import Vysledky from "../chapters/vysledkyAVyhodnoceni.mdx";
import { ScrollProgress } from "../components/ScrollProgress";
import { Navigation } from "../components/Navigation";

export const metadata = {
  title: "Strojové učení – Predikce hodnocení videoher",
};

export default function Home() {
  return (
    <>
      <ScrollProgress />
      <Navigation
        links={[
          { id: "#uvod", label: "Úvod a definice rozhodovacího problému" },
          { id: "#ziskaniDat", label: "Získání dat" },
          { id: "#analyzaDat", label: "Analýza dat" },
          { id: "#predzpracovaniDat", label: "Předzpracování dat" },
          { id: "#vyberModelu", label: "Výběr modelů" },
          { id: "#trenovaniModelu", label: "Trénování modelů" },
          { id: "#vysledkyAVyhodnoceni", label: "Výsledky a Vyhodnocení" },

        ]}
      />
      <main className="container" style={{ maxWidth: "80ch" }}>
        <hgroup>
          <h1>Strojové učení – Predikce hodnocení videoher</h1>
          <h3>Tomáš Lacina, Adam Prchal</h3>
        </hgroup>

        <Uvod />
        <ZiskaniDat />
        <AnalyzaDat />
        <PredzpracovaniDat />
        <VyberModelu />
        <TrenovaniModelu />
        <Vysledky />
      </main>
    </>
  );
}
