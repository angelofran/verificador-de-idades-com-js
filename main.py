function clicou(){
    let data = new Date()
    var ano_actual = data.getFullYear()
    var res = document.getElementById('res')
    var input = document.getElementById('input')
    if (input.value == 0 || input.value  > ano_actual){
        alert('[Erro] digite correctamente!')
    } else {
        var radsex = window.document.getElementsByName('radio1')
        var idade = ano_actual - Number(input.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        img.style.width = '100px'
        img.style.height = '100px'
        if (radsex[0].checked){
            var genero = 'masculino'
            if ( idade >= 0 && idade < 10){
                img.setAttribute('src', 'https://st2.depositphotos.com/1003940/5526/i/450/depositphotos_55260497-stock-photo-cute-happy-baby-boy-crawling.jpg')
            } else if (idade < 21){
                img.setAttribute('src', 'https://dtpr0iglcwflm.cloudfront.net/profissoes/wp-content/uploads/2019/08/7-passos-para-fazer-curriculo-de-jovem-aprendiz-scaled-1600x900.jpg')
            } else if (idade < 50){
                img.setAttribute('src', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCBZ0Gw40LXvN-As6La6LnmnMDD11Rqb0zL70E2Yve5wG-GpwS5iu88p9ZVVE2rXjFEr8&usqp=CAU')
            }else {
                img.setAttribute('src', 'https://corasenior.com.br/wp-content/uploads/elementor/thumbs/idoso-sociedade-cora-residencial-para-idosos-ova5juvui2agrp7ez89ttb61pnwqs5wx52tykaeyjc.jpg')
            }
        }else if (radsex[1].checked){
            var genero = 'femenino'
            if ( idade >= 0 && idade < 10){
                img.setAttribute('src', 'https://img.freepik.com/fotos-gratis/o-pequeno-bebe-encontra-se-na-cama_8353-5187.jpg?w=360')
            } else if (idade < 21){
                img.setAttribute('src', 'https://st.depositphotos.com/1345889/2318/i/450/depositphotos_23186830-stock-photo-cute-young-student-girl.jpg')
            } else if (idade < 50){
                img.setAttribute('src', 'http://www.altavision.com.co/adulto')
            }else {
                img.setAttribute('src', 'https://regenerati.com.br/wp-content/uploads/2022/02/papel-do-idoso-na-sociedade.jpg')
            }
        }
        var p = document.getElementsByName('paragrafo')
        p.innerText = ''
        res.style.textAlign = 'center'
        res.innerHTML = `Você tem ${idade} ano(s).<br>`
        image = res.appendChild(img)
    }


    }
