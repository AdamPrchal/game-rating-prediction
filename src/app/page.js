import Uvod from "../chapters/uvod.mdx";
import ZiskaniDat from "../chapters/ziskaniDat.mdx";
import AnalyzaDat from "../chapters/analyzaDat.mdx";
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
            {id: "#analyzaDat", label:" Analýza dat"},
        ]}
      />
      <main className="container" style={{ maxWidth: "70ch" }}>
        <hgroup>
          <h1>Strojové učení – Predikce hodnocení videoher</h1>
          <h3>Tomáš Lacina, Adam Prchal</h3>
        </hgroup>

        <Uvod />
        <ZiskaniDat />
          <AnalyzaDat />
      </main>
    </>
  );
}
