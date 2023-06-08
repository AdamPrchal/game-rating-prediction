import Uvod from "../chapters/uvod.mdx";
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
        ]}
      />
      <main className="container" style={{ maxWidth: "70ch" }}>
        <hgroup>
          <h1>Strojové učení – Predikce hodnocení videoher</h1>
          <h3>Tomáš Lacina, Adam Prchal</h3>
        </hgroup>

        <Uvod />
      </main>
    </>
  );
}
