var knapoverskrift = document.getElementById('leggtiloverskrift')
var knaptekst = document.getElementById('leggetiltekst')
var knapfarge = document.getElementById('bytterfarge')
var knaptekstfarge = document.getElementById('endretekstfarge')
var knapflytttekstvenstre = document.getElementById('flytttekstenvenstre')
var knapflyttteksthøyre = document.getElementById('flytttekstenhøyre')
var knapliste = document.getElementById('leggtilliste')
var knapbilde = document.getElementById('leggtilbilde')

knapoverskrift.addEventListener('click', leggtiloverskrift)
knaptekst.addEventListener('click', leggetiltekst)
knapfarge.addEventListener('click', bytterfarge)
knaptekstfarge.addEventListener('click', endretekstfarge)
knapflytttekstvenstre.addEventListener('click', flytttekstenvenstre)
knapflyttteksthøyre.addEventListener('click', flytttekstenhøyre)
knapliste.addEventListener('click', leggtilliste)
knapbilde.addEventListener('click', leggtilbilde)


/** endrer bakgrunsfargen på nettsiden*/
function bytterfarge() {
    var farge = document.getElementById('fargeinn').value
    if (farge === "Martin") {
        farger = ['red', 'blue', 'green']
        farge = farger[Math.floor(Math.random() * farger.length)]
    }
    document.getElementById('høyre').style.backgroundColor = farge
}
/** Legger til tekst på netsiden*/
function leggetiltekst() {
    var tekst = document.getElementById('tekstinn').value
    document.getElementById('fintekst').innerText
    = tekst
}
/** Legger til en overskrift på netsiden*/
function leggtiloverskrift() {
    var overskrift = document.getElementById('overskriftinn').value
    document.getElementById('overskrift').innerText
    = overskrift
}
/** endrer teksten sin farge som du la til*/
function endretekstfarge() {
    var tekstfarge = document.getElementById('tekstfarge').value
    document.getElementById('fintekst').style.color = tekstfarge
}
/**Flytter teksten til siden*/
var flytttekst = 10
function flytttekstenhøyre(){
    flytttekst = flytttekst + 10
    document.getElementById('fintekst').style.paddingLeft = flytttekst + 'px'
    document.getElementById('overskrift').style.paddingLeft = flytttekst + 'px' 
    document.getElementById('minliste').style.paddingLeft = flytttekst + 'px'
}
function flytttekstenvenstre(){
    flytttekst = flytttekst - 10
    document.getElementById('fintekst').style.paddingLeft = flytttekst + 'px'
    document.getElementById('fintekst').style.paddingLeft = flytttekst + 'px'
    document.getElementById('overskrift').style.paddingLeft = flytttekst + 'px' 
    document.getElementById('minliste').style.paddingLeft = flytttekst + 'px'
}

/** legger til en liste på nettsiden*/
function leggtilliste() {
    var liste = document.getElementById('listeinn').value
    
    document.getElementById('minliste').innerHTML += ('<li>'+ liste + '</li>')
    }   
    /** legger til et random bilde på netsiden velger mellom de ulike bildene*/
function leggtilbilde() {
    bilder = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11','12', 'favurittbilde']
    randombildeut = bilder[Math.floor(Math.random() * bilder.length)]
    document.getElementById('bilde').innerHTML += ('<img id=bilder src="static/bilder/'+ randombildeut +'.jpg" alt="fint bilde">')
}