import Introduction from "../../chapters/text-mining/introduction.mdx";
import TextRepresentation from "../../chapters/text-mining/textRepresentation.mdx";
import ResultsAndEvaluation from "../../chapters/text-mining/resultsAndEvaluation.mdx";
import DataCollection from "../../chapters/text-mining/dataCollection.mdx";
import SentimentAnalysis from "../../chapters/text-mining/sentimentAnalysis.mdx";
import DataAnalysis from "../../chapters/text-mining/dataAnalysis.mdx";
import Classification from "../../chapters/text-mining/classification.mdx";

import { ScrollProgress } from "../../components/ScrollProgress";
import { Navigation } from "../../components/Navigation";

export const metadata = {
  title: "Text mining – Game reviews analysis",
};

export default function Home() {
  return (
    <>
      <ScrollProgress />
      <Navigation
        links={[
          { id: "#introduction", label: "Introduction and Definition of Analysis Goal" },
  { id: "#dataCollection", label: "Data Collection" },
  { id: "#sentimentAnalysis", label: "Sentiment Analysis" },
  { id: "#dataAnalysis", label: "Data Analysis" },
  { id: "#classification", label: "Classification" },
  { id: "#resultsAndEvaluation", label: "Final Summary" },
        ]}
      />
      <main className="container prose" style={{ maxWidth: "80ch" }}>
        <hgroup>
          <h1>Text mining – Game reviews analysis</h1>
          <h3>Tomáš Lacina, Adam Prchal</h3>
        </hgroup>

        <Introduction />
        <DataCollection />
        <TextRepresentation />
        <SentimentAnalysis />
        <DataAnalysis />
        <Classification />
        <ResultsAndEvaluation />
      </main>
    </>
  );
}
