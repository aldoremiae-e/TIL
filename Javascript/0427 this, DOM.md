# 0427 js_2

[TOC]

## ๐ฃthis

1. class ๋ด๋ถ์ ์์ฑ์ ํจ์๋ฅผ ๊ฐ๋ฆฌํด
2. ๋ฉ์๋๋ฅผ ๊ฐ๋ฆฌํด
3. ๊ทธ ์ธ window๋ฅผ ๊ฐ๋ฆฌํด

```javascript
const me = {
    firstName : 'Miae',
    lastName : 'Kim',
    fullName : this.firstName + this.lastName,
    getFullName : function(){
        return this.firstName + this.lastName
    }
}
```

this๋ class ๋ด๋ถ์ ์์ฑ์ ํจ์๋ฅผ ๊ฐ๋ฆฌํด

```javascript
> me.fullName
> NaN

> me.getFullName()
> MiaeKim // this === me

> getFullName()
> ์๋ฌ๋ธ
```

๋ฉ์๋์์๋ this๊ฐ me๋ฅผ ๊ฐ๋ฆฌํด



```javascript
function getFullName() {
    return this.firstName + this.lastName
}

const you = {
    firstName : 'Tony',
    lastName : 'Stark',
    getFullName : getFullName
}

> you.getFullName()
> 'TonyStark' //this === you

> getFullName()
> NaN //this === window
```

๋ฉ์๋์์ this๋ you๋ฅผ ๊ฐ๋ฆฌํด

### ๐ค function ํค์๋์ ํ์ดํ ํจ์์ ์ฐจ์ด

- forEach์ ์ฝ๋ฐฑํจ์์ ๊ฒฝ์ฐ ๋ฉ์๋๊ฐ this.___๋ ๋ฉ์๋๊ฐ ์๋๊ธฐ ๋๋ฌธ์ ํธ์ถ ๋ถ๊ฐ๋ฅํ๋ค

  - ๋๋ฌธ์ ์ฝ๋ฐฑํจ์ ๋ด๋ถ์ this๋ window๊ฐ ๋๊ธฐ ๋๋ฌธ์ ๊ฐ์ฒด ๋ด๋ถ๋ก ์ ๊ทผ ๋ถ๊ฐ๋ฅํ๋ค

    - ์ฝ๋ฐฑํจ์ ๋ด๋ถ์ ์ ๊ทผํ๊ธฐ ์ํด **.bind(this) ๋ฉ์๋**๋ฅผ ์ฌ์ฉํด์ผํ๋ค

      - ๋ฒ๊ฑฐ๋ก์์ ๊ทน๋ณตํ ๊ฒ์ด ํ์ดํ ํจ์

      

  - ํจ์ ๋ด๋ถ์ this ํค์๋๊ฐ ์กด์ฌํ  ๊ฒฝ์ฐ

    - ํ์ดํ ํจ์์ function ํค์๋๋ก ์ ์ธํ ํจ์๊ฐ ๋ค๋ฅด๊ฒ ๋์ํ๋ค.

  - ํจ์ ๋ด๋ถ์ this ํค์๋๊ฐ ์กด์ฌํ์ง ์์ ๊ฒฝ์ฐ

    - ํ์ดํ ํจ์์ function ํค์๋๋ก ์ ์ธํ ํจ์๊ฐ ์์ ํ ๋์ผํ๊ฒ ๋์ํ๋ค.



## ๐ฃlodash

> A modern JavaScript utility library

- ๋ชจ๋์ฑ, ์ฑ๋ฅ ๋ฐ ์ถ๊ฐ ๊ธฐ๋ฅ์ ์ ๊ณตํ๋ JavaScript ์ ํธ๋ฆฌํฐ ๋ผ์ด๋ธ๋ฌ๋ฆฌ
- array, object ๋ฑ ์๋ฃ๊ตฌ์กฐ๋ฅผ ๋ค๋ฃฐ ๋ ์ฌ์ฉํ๋ ์ ์ฉํ๊ณ  ๊ฐํธํ ์ ํธ๋ฆฌํฐ ํจ์๋ค ์ ๊ณต

- lodash๋ฅผ ์ฌ์ฉํ์ง ์์ ๊ฒฝ์ฐ, ๊น์ ๋ณต์ฌ๋ ์ง์  ํจ์๋ฅผ ๋ง๋ค์ด์ ๊ตฌํํด์ผํ๋ค.



## ๐ฃJS ์ญ์ฌ

### ๐ค ๋ธ๋๋ ์์ดํฌ

- JS ์ต์ด ์ค๊ณ์
- ๋ชจ์ง๋ผ ์ฌ๋จ ๊ณต๋ ์ค๋ฆฝ์
- ์ฝ๋๋ค์ ํผ๋์ค ํ๋ก์ ํธ ์งํ - ํ์ด์ดํญ์ค์ ์ ์ 

> ํํธํ => ํ์คํ

- ์  1์ฐจ ๋ธ๋ผ์ฐ์  ์ ์ ์ดํ ์ฌ๋ฌ ๋ธ๋ผ์ฐ์ ์์ ์์ฒด JS ์ธ์ด๋ฅผ ์ฌ์ฉ
- ํฌ๋ก์ค ๋ธ๋ผ์ฐ์ง ์ด์ ๋ฐ์
  - ํ์คํ์ ํ์์ฑ์ด ์๊น
    - Vanilla JavaScript



## ๐ฃDOM & BOM

### ๐คDOM

> Document Object Model

- HTML, XML ๊ฐ์ ๋ฌธ์๋ฅผ ๋ค๋ฃจ๊ธฐ ์ํ ๋ฌธ์ ํ๋ก๊ทธ๋๋ฐ ์ธํฐํ์ด์ค

- ๋ผ๋ฆฌ์  ํธ๋ฆฌ ๋ชจ๋ธ : ๋ฌธ์๋ฅผ **๊ตฌ์กฐํ**ํ๊ณ , ๊ตฌ์กฐํ๋ **๊ตฌ์ฑ ์์**๋ฅผ ํ๋์ **๊ฐ์ฒด**๋ก ์ทจ๊ธ

<img src="0427.assets/image-20220502033522831.png" alt="image-20220502033522831" style="zoom:50%;" />

- ๋จ์ํ ์์ฑ ์ ๊ทผ, ๋ฉ์๋ ํ์ฉ ๋ฟ๋ง ์๋๋ผ, ํ๋ก๊ทธ๋๋ฐ ์ธ์ด ํน์ฑ์ ํ์ฉํ ์กฐ์ ๊ฐ๋ฅ( ๋ฐ๋ณต, ์กฐ๊ฑด )
  - ์ฃผ์ ๊ฐ์ฒด
    - window : DOM์ ํํํ๋ ์ฐฝ, ์ต์์ ๊ฐ์ฒด (์๋ต ๊ฐ๋ฅ)
    - document : ํ์ด์ง ์ปจํ์ธ ์ Entry Point, <body>๊ฐ์ ๊ตฌ์ฑ ์์(๊ฐ์ฒด ์ทจ๊ธ)์ ํฌํจ
    - ๊ทธ ์ธ : navigator, location, history, screen

- **Pasing** (ํ์ฑ)

  > ํด์ : ๋ธ๋ผ์ฐ์ ๊ฐ ๋ฌธ์์ด์ ํด์ํ์ฌ DOM tree๋ก ๋ง๋๋ ๊ณผ์ 



### ๐คBOM

> Browser Object Model

- ์๋ฐ์คํฌ๋ฆฝํธ๊ฐ ๋ธ๋ผ์ฐ์ ์ ์ํตํ๊ธฐ ์ํ ๋ชจ๋ธ
- ๋ธ๋ผ์ฐ์ ์ ์ฐฝ, ํ๋ ์์ ์ถ์ํํด์ ํ๋ก๊ทธ๋๋ฐ์ ์ผ๋ก ์ ์ดํ  ์ ์๋๋ก ์ ๊ณตํ๋ ์๋จ
- **window ๊ฐ์ฒด** ๋ ๋ชจ๋  ๋ธ๋ผ์ฐ์ ๋ก๋ถํฐ ์ง์๋ฐ๊ณ , **๋ธ๋ผ์ฐ์ ์ ์ฐฝ**๋ฅผ ์ง์นญ



## ๐ฃDOM ์กฐ์

> Document๋ ๋ฌธ์ ํ ์ฅ์ ํด๋นํ๊ณ , ์ด๋ฅผ ์กฐ์

- ์กฐ์ ์์ : 1. ์ ํ(Select) 2. ๋ณ๊ฒฝ(Manipulation)

- DOM ๊ด๋ จ ๊ฐ์ฒด์ ์์ ๊ตฌ์กฐ

  

<img src="0427.assets/image-20220502034721239.png" alt="image-20220502034721239" style="zoom:50%;" />



### ๐ค DOM ์ ํ - `document.querySelector()`

- querySelector, querySelectorAll()์ ์ฌ์ฉํ๋ ์ด์  :
  - id, class, tag์ ํ์ ๋ฑ์ ๋ชจ๋ ์ฌ์ฉ ๊ฐ๋ฅํ๋ฏ๋ก, ๋ ๊ตฌ์ฒด์ ์ด๊ณ  ์ ์ฐํ๊ฒ ์ ํ์ด ๊ฐ๋ฅํ๋ค

- `document.querySelector(selector)`
  - ์ ๊ณตํ ์ ํ์์ ์ผ์นํ๋ element ํ๋ ์ ํ
  - ์ ๊ณตํ CSS selector๋ฅผ ๋ง์กฑํ๋ ์ฒซ๋ฒ ์งธ element ๊ฐ์ฒด๋ฅผ ๋ฐํ ,  ์์ผ๋ฉด null
- `document.querySelectorAll(selector)`
  - ์ ๊ณตํ ์ ํ์์ ์ผ์นํ๋ ์ฌ๋ฌ element ์ ํ
  - ๋งค์นญ ํ  ํ๋ ์ด์์ selector๋ฅผ ํฌํจํ๋ CSS selector๋ฅผ ๋ฌธ์์ด๋ก ๋ฐ์
  - ์ง์ ๋ ์๋ ํฐ์ ์ผ์นํ๋ Nodelist๋ฅผ ๋ฐํ



### HTML Collection & NodeList

- ๋ ๋ค ๋ฐฐ์ด๊ณผ ๊ฐ์ด, ๊ฐ ํญ๋ชฉ์ ์ ๊ทผํ๊ธฐ ์ํ index ์ ๊ณต

  | HTML collection                              | NodeList                                                     |
  | -------------------------------------------- | ------------------------------------------------------------ |
  | name, id, index ์์ฑ์ผ๋ก ๊ฐ ํญ๋ชฉ์ ์ ๊ทผ ๊ฐ๋ฅ | index๋ก๋ง ๊ฐ ํญ๋ชฉ์ ์ ๊ทผ ๊ฐ๋ฅ                                |
  | ๋ฉ์๋ ์ฌ์ฉ ๋ถ๊ฐ                             | ๋ฐฐ์ด์์ ์ฌ์ฉํ๋ forEach ๋ฉ์๋ ๋ฑ ๋ค์ํ ๋ฉ์๋ ์ฌ์ฉ ๊ฐ๋ฅ  |
  | Live Collection => DOM ๋ณ๊ฒฝ์ฌํญ ์ค์๊ฐ ๋ฐ์  | Live Collection => DOM ๋ณ๊ฒฝ์ฌํญ ์ค์๊ฐ ๋ฐ์<br /><br />*๋จ, guerySelectorAll()์ ์ํด ๋ฐํ๋๋ NodeList๋ Static Collection์ผ๋ก ์ค์๊ฐ ๋ฐ์์ ์๋จ* |

  

### ๐ค DOM ๋ณ๊ฒฝ - `Create, append, innerText, innerHTML`

- document.creatElement()

  - ์์ฑํ ํ๊ทธ ๋ช์ HTML ์์๋ฅผ ์์ฑํ์ฌ ๋ฐํ

    ![image-20220502040743936](0427.assets/image-20220502040743936.png)

- Element.append()

  - ํน์  ๋ถ๋ชจ Node์ ์์ NodeList ์ค ๋ง์ง๋ง ์์ ๋ค์์ Node๊ฐ์ฒด๋ DOMString์ ์ฝ์

    <img src="0427.assets/image-20220502040801558.png" alt="image-20220502040801558" style="zoom:50%;" />

  - ์ฌ๋ฌ๊ฐ์ Node ๊ฐ์ฒด๋ DOMString ์ถ๊ฐ ๊ฐ๋ฅ

    <img src="0427.assets/image-20220502040721558.png" alt="image-20220502040721558" style="zoom:50%;" />

  - ๋ฐํ ๊ฐ ์์

- Node.appendChild()

  - ํ Node๋ฅผ ํน์  ๋ถ๋ชจ Node์ ์์ NodeList ์ค ๋ง์ง๋ง ์์์ผ๋ก ์ฝ์ (Node๋ง ์ถ๊ฐ ๊ฐ๋ฅ)

    ![image-20220502041005954](0427.assets/image-20220502041005954.png)

  - ํ๋ฒ์ ํ๋์ Node ๋ง ๊ฐ๋ฅ

| ๋ถ๋ชจNode.append()                | Node.appendChild()            |
| -------------------------------- | ----------------------------- |
| ๋ฌธ์์ด ๊ฐ์ฒด ์ถ๊ฐ ๊ฐ๋ฅ            | ๋ฌธ์์ด ์๋จ, Node ๊ฐ์ฒด๋ง ํ์ฉ |
| ๋ฐํ๊ฐ ์์                      | ์ถ๊ฐ๋ Node๊ฐ์ฒด ๊ฐ ๋ฐํ       |
| ์ฌ๋ฌ Node๊ฐ์ฒด์ ๋ฌธ์์ด ์ถ๊ฐ ๊ฐ๋ฅ | ํ๋์ Node ๊ฐ์ฒด๋ง ์ถ๊ฐ ๊ฐ๋ฅ  |



- Node.innerText

  ```javascript
  new1.innerText = '<li>์ถ์ฒ</li>'
  > <li>์ถ์ฒ</li>
  ```

  

  - Node ๊ฐ์ฒด์ ๊ทธ ์์์ ํ์คํธ ์ปจํ์ธ ๋ฅผ ํํ
  - ์ต์ข์ ์ผ๋ก ์คํ์ผ๋ง์ด ์ ์ฉ๋๋ ๋ชจ์ต์ผ๋ก ํํ

- Element.innerHTML

  ```javascript
  new1.innerHTML = '<li>์ถ์ฒ</li>'
  > ์ถ์ฒ
  ```

  

  - ์์ ๋ด์ ํฌํจ๋ HTML ๋งํฌ์์ ๋ฐํ
  - XSS (cross-site Scripting) ๊ณต๊ฒฉ์ ์ทจ์ฝํ๋ฏ๋ก ์ฌ์ฉ ์ ์ฃผ์



### ๐ค DOM ์ญ์  - `ChildNode.remove() , Node.removeChild()`

- ChildNode.remove()

  ![image-20220502042212897](0427.assets/image-20220502042212897.png)

  - Node๊ฐ ์ํ ํธ๋ฆฌ์์ ํด๋น ๋ธ๋ ์ ๊ฑฐ

- Node.removeChild()

  ![image-20220502042201182](0427.assets/image-20220502042201182.png)

  - DOM์์ ์์ Node๋ฅผ ์ ๊ฑฐํ๊ณ  ์ ๊ฑฐ๋ Node๋ฅผ ๋ฐํ
  - Node๋ ์ธ์๋ก ๋ค์ด๊ฐ๋ ์์ ๋ธ๋์ ๋ถ๋ชจ ๋ธ๋



### ๐ค DOM ์์ฑ - `Element.setAttribute(name, value), Element.getAttribute(attributeName)`

- Element.setAttribute(name, value)

  ```javascript
  const header = document.querySelector('#location-header')
  header.setAttribute('class', 'ssafy-location')
  ```

  

  - ์ง์ ๋ ์์์ ๊ฐ์ ์ค์ 
  - ์์ฑ์ด ์กด์ฌํ๋ฉด ๊ฐ์ ๊ฐฑ์ , ์กด์ฌํ์ง ์์ผ๋ฉด ์ง์ ๋ ์ด๋ฆ๊ณผ ๊ฐ์ผ๋ก ์ ์์ฑ ์ค์ 

- Element.getAttribute(attributeName)

  ```javascript
  const geta = document.querySelector('.ssafy-location') //.์ ๋ถ์ธ๋ค
  geta.getAttribute('class')
  > 'ssafy-location'
  ```

  

  - ํด๋น ์์์ ์ง์ ๋ ๊ฐ์ ๋ฐํ
  - ์ธ์๋ ๊ฐ์ ์ป๊ณ ์ ํ๋ ์์ฑ์ ์ด๋ฆ



## ๐ฃEvent

> ๋คํธ์ํฌ ํ๋์ด๋ ์ฌ์ฉ์์์ ์ํธ์์ฉ ๊ฐ์ ์ฌ๊ฑด์ ๋ฐ์์ ์๋ฆฌ๊ธฐ ์ํ ๊ฐ์ฒด

- ์ญํ  : "ํน์  ์ด๋ฒคํธ๊ฐ ๋ฐ์**ํ๋ฉด,** ํ ์ผ์ ๋ฑ๋ก**ํ๋ค.**"



### ๐ค EventTarget.addEventListener(type, listener)

 1. ์ ํ : EventTarget = document.querySelector()

    ```javascript
    const myCI = document.querySeletor('#my-change-input')
    ```

    

 2. ๋ฏธ๋ฆฌ ํจ์๋ฅผ ๋ง๋ ๋ค๋ฉด : 

    ```javascript
    const changeColor = function(event) {
        const h2Tag = document.querySelector('h2')
        h2Tag.style.color = event.target.value // ์์ฒญํ ๊ฐ์ ์ด๋ฒคํธ ํ๊ฒ์ผ๋ก ํจ
    }
    ```

    

 3. EventTarget.addEventListener('์๋', ํจ์(event){ ๋ด์ฉ})

    ํน์ EventTarget.addEventListener('์๋', ํจ์์ด๋ฆ)

    ```javascript
    myCI.addEventListener('input', changeColor)
    ```

    

### ๐คevent.preventDefault()

- ํ์ฌ ์ด๋ฒคํธ์ ๊ธฐ๋ณธ ๋์์ ์ค๋จ