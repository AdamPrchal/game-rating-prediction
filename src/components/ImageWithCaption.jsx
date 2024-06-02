import React from "react";



export const ImageWithCaption = ({ src, caption, source, lang}) => {
  return (
    <figure>
      <img src={src} alt={caption} />
      <figcaption style={{fontSize: "0.75rem"}}>
        {caption} {source && <a href={source}>{lang === "cs" ? "Zdroj" : "Source"}</a>}
      </figcaption>
    </figure>
  );
};
