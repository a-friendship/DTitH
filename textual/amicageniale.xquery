xquery version "3.0";

declare namespace tei="http://www.tei-c.org/ns/1.0";

declare function local:howManyPers($node as node()) 
    {
    count($node/tei:p/tei:persName)
    };

declare function local:howManyDates($node as node()) 
    {
    count($node/tei:p/tei:date)
    };

declare function local:howManyThisPerson($node as node()) 
    {
    count($node/tei:p/tei:persName[@ref='#AchilleCarracci'])
    };

let $ourfile := doc("/Users/martinapensalfini/Documents/Digital Texts In Humanities/infanziasep.xml")
    for $div in $ourfile/tei:TEI/tei:text/tei:body/tei:div/tei:div
        return (local:howManyDates($div))