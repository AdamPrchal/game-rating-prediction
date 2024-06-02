import Uvod from "../../chapters/strojove-uceni/uvod.mdx";
import ZiskaniDat from "../../chapters/strojove-uceni/ziskaniDat.mdx";
import AnalyzaDat from "../../chapters/strojove-uceni/analyzaDat.mdx";
import VyberModelu from "../../chapters/strojove-uceni/vyberModelu.mdx";
import TrenovaniModelu from "../../chapters/strojove-uceni/trenovaniModelu.mdx";
import PredzpracovaniDat from "../../chapters/strojove-uceni/predzpracovaniDat.mdx";
import Vysledky from "../../chapters/strojove-uceni/vysledkyAVyhodnoceni.mdx";
import { ScrollProgress } from "../../components/ScrollProgress";
import { Navigation } from "../../components/Navigation";

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
