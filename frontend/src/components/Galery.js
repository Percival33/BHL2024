import {Card} from "./Card";
import {useState} from "react";

export function Gallery(props) {
    const [cards, setCards] = useState(props.cards);
    // const card = cards[0];
    // console.log(card);
    return (
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {cards.map((card) => (
                <Card {...card} key={card.key}/>
            ))}
        </div>
    );
}
