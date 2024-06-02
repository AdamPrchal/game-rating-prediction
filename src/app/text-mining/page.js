import Introduction from "../../chapters/text-mining/introduction.mdx";
import DataPreprocessing from "../../chapters/text-mining/dataPreprocessing.mdx";
import ResultsAndEvaluation from "../../chapters/text-mining/resultsAndEvaluation.mdx";
import DataAnalysis from "../../chapters/text-mining/dataAnalysis.mdx";

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
          { id: "#introduction", label: "Introduction and Definition of Analysis Goal" },
  { id: "#dataAnalysis", label: "Data Analysis" },
  { id: "#dataPreprocessing", label: "Data Preprocessing" },
  { id: "#resultsAndEvaluation", label: "Results and Evaluation" },
        ]}
      />
      <main className="container" style={{ maxWidth: "80ch" }}>
        <hgroup>
          <h1>Text mining – Game reviews analysis</h1>
          <h3>Tomáš Lacina, Adam Prchal</h3>
        </hgroup>

        <Introduction />
        <DataAnalysis />
        <DataPreprocessing />
        <ResultsAndEvaluation />
      </main>
    </>
  );
}
