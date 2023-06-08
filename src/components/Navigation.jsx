import React from "react";

export const Navigation = ({ links }) => {
  return (
    <nav style={{ position: "fixed", top: "1rem", right: "1rem" }}>
      <ul>
        <li role="list" dir="rtl">
          <details role="list">
            <summary aria-haspopup="listbox" role="button">
              Jít na kapitolu
            </summary>
            <ul role="listbox">
              {links.map((item) => (
                <li key={item.id}>
                  <a href={item.id}>{item.label}</a>
                </li>
              ))}
            </ul>
          </details>
        </li>
      </ul>
    </nav>
  );
};
