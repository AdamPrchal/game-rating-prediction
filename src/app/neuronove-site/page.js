import Uvod from "../../chapters/neuronove-site/uvod.mdx";
import TvorbaModelu from "../../chapters/neuronove-site/tvorbaModelu.mdx";
import PredzpracovaniDat from "../../chapters/neuronove-site/predzpracovaniDat.mdx";
import Vysledky from "../../chapters/neuronove-site/vysledkyAVyhodnoceni.mdx";
import AnalyzaDat from "../../chapters/neuronove-site/analyzaDat.mdx";

import { ScrollProgress } from "../../components/ScrollProgress";
import { Navigation } from "../../components/Navigation";

export const metadata = {
  title: "Neuronové sítě – Predikce hodnocení videoher",
};

export default function Home() {
  return (
    <>
      <ScrollProgress />
      <Navigation
        links={[
          { id: "#uvod", label: "Úvod a definice rozhodovacího problému" },
          { id: "#analyzaDat", label: "Analýza dat" },
          { id: "#predzpracovaniDat", label: "Předzpracování dat" },
          { id: "#tvorbaModelu", label: "Tvorba modelů" },
          { id: "#vysledkyAVyhodnoceni", label: "Výsledky a Vyhodnocení" },
        ]}
      />
      <main className="container" style={{ maxWidth: "80ch" }}>
        <hgroup>
          <h1>Neuronové sítě – Predikce hodnocení videoher</h1>
          <h3>Tomáš Lacina, Adam Prchal</h3>
        </hgroup>

        <Uvod />
        <AnalyzaDat />
        <PredzpracovaniDat />
        <TvorbaModelu />
        <Vysledky />
      </main>
    </>
  );
}
