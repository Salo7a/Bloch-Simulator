<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
# MRI Task 1 Report

| Name                    | Section | Bench Number |
|-------------------------|---------|-------------:|
| Ahmed Salah El-Din      | 1       |            5 |
| Ahmed Adel Ahmed        | 1       |           6  |
| Salma Ayman Ahmed       | 1       |           37 |
| Abdullah Mohammed Sabry | 2       |            8 |

Fourier Transform
---

By applying the Discrete Fast Fourier Transform method, we obtained the Fourier Transform of an image, we then plotted its Components (Magnitude, Phase, Real Part, Imaginary Part) Separately.

---

Magnitude of an Image:

---

![alt text](Mag.png "Magnitude of the Fourier Transform of an image")

---

It's Phase

---

![alt text](Phase.png "Phase of the Fourier Transform of an image")

---

Non-Uniform Magnetic Field
---

We created a function that simulates the non-uniformity of a magnet, giving it the theoretical magnetic flux density in Tesla, maximum deviation due to the non-uniformity and the length of the magnet, using this data it generates a random curve we then plot this curve in our program.

---

![alt text](Nonuniform.png "The generated curve of the non-uniformity effect.")

---
Relaxation Process
---

It’s a process where the spins, which received a Radio Frequency pulse which caused it to change the direction of its field, to release the energy it received from the pulse while returning to its original position

---

The following image demonstrates the Rotating Frame

---

![alt text](Relaxation.gif "Rotating Frame.")

---

The Precession

---

![alt text](Precess.gif "The Precession.")

---
Bloch Equation Simulation
---


![alt text](Bloch.png "Bloch Equation.")

###### Pulse Repetition Time (TR)
the red line in the plot explain the time between 2 successive RF pulse sequence

![equation](sadsa)

 $\alpha$

$$e = mc^2$$

<html>
<head>
<title>MathJax TeX Test Page</title>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
</script>
</head>
<body>
When \(a \ne 0\), there are two solutions to \(ax^2 + bx + c = 0\) and they are
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$
</body>
</html>
