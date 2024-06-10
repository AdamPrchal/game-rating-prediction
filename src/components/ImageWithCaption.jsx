import React from "react";



export const ImageWithCaption = ({ src, caption, source, lang}) => {
  return (
    <figure>
      <a href={src} target="_blank" className="not-prose">
       <img src={src} alt={caption} />
      </a>
      <figcaption style={{fontSize: "0.75rem"}}>
        {caption} {source && <a href={source}>{lang === "cs" ? "Zdroj" : "Source"}</a>}
      </figcaption>
    </figure>
  );
};
