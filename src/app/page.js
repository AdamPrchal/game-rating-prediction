import Image from "next/image";
import Link from "next/link";

export const metadata = {
  title: "Predikce hodnocení videoher",
};

export default function Home() {
  return (
    <>
      <main className="container" style={{ maxWidth: "80ch" }}>

      <section>
          <hgroup>
            <h1>Game reviews analysis</h1>
            <h3>Tomáš Lacina, Adam Prchal</h3>
          </hgroup>
          <div className="menu">
            <div className="menu__item">
              <Image
                src={"/text-mining.webp"}
                width={200}
                height={200}
                style={{ marginBottom: "1rem" }}
                className="menu__image"
              />
              <Link href={"/text-mining"}>
                <button href="#" role="button" className="secondary outline">
                  Text mining ➜
                </button>
              </Link>
            </div>
          </div>
        </section>
        <section>
          <hgroup>
            <h1>Predikce hodnocení videoher</h1>
            <h3>Tomáš Lacina, Adam Prchal</h3>
          </hgroup>
          <div className="menu">
            <div className="menu__item">
              <Image
                src={"/strojove-uceni.png"}
                width={200}
                height={200}
                style={{ marginBottom: "1rem" }}
                className="menu__image"
              />
              <Link href={"/strojove-uceni"}>
                <button href="#" role="button" className="secondary outline">
                  Strojové učení ➜
                </button>
              </Link>
            </div>
            <div className="menu__item">
              <Image
                src={"/neuronove-site.png"}
                width={200}
                height={200}
                style={{ marginBottom: "1rem" }}
                className="menu__image"
              />
              <Link href={"/neuronove-site"}>
                <button href="#" role="button" className="secondary outline">
                  Neuronové sítě ➜
                </button>
              </Link>
            </div>
          </div>
        </section>
  
      </main>
    </>
  );
}
