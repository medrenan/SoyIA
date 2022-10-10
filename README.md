<h1 align="center">
        <img src="https://github.com/medrenan/SoyIA/blob/main/doc/Imagens/Logo/logo.png" alt="Logo SoyIA" width="220px" height="220px">
</h1>
<p align="center">
        <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" alt="Tensorflow Badg">
        <img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white" alt="Keras Badge">
        <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Badge">
        <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL Badge">
</p>

<h2 align="right">
        <img src="https://img.shields.io/badge/status-ongoing-blue?style=for-the-badge&logo=appveyor" alt="Status: Ongoing">   
        <img src="https://img.shields.io/badge/sprint-2-blue?style=for-the-badge&logo=appveyor" alt="Second= sprint">
</h2>
            

# Index 📎

- [Index 📎](#index-)
- [About 📚](#about-)
- [Product Backlog 📍](#product-backlog-)
- [Project in Operation 📱](#project-in-operation-)
- [Delivery Schedule 🗓](#delivery-schedule-)
- [Team 👩‍💻👨‍💻](#team-)

# About 📚

<p align="justify">The project constitutes an addition of a new tool to an application made in another project for Visiona. In this tool it was necessary to go to the field to count pods and grains for its use and this required time from the farmer,the idea of creating a tool with artificial intelligence for automatic and visual counting of these grains was created and given to us to develop.</p>

# Product Backlog 📍

<p align= "justigy"> It was decided that the project would be divided into 4 deliveries, throughout the sprints it will be updated and modified as the deliveries progress.</p>
<p align="justify">
        <img src="https://github.com/medrenan/SoyIA/blob/main/doc/Product%20Backlog/Product%20Backlog%20Sprint%201.png" width="400"/>
        <img src="https://github.com/medrenan/SoyIA/blob/main/doc/Product%20Backlog/Product%20Backlog%20Sprint%202.png" width="400"/>
        

You can also see the complete *Product Backlog* of each sprint clicking [here](https://docs.google.com/spreadsheets/d/1kvREkN38lj2lWdEc1EylQo3yAcwkrQTZlOtGEeqNCi8/edit?usp=sharing)
</p>

# Project in Operation 📱

<p align="justify">
  Result of the AI ​​model trained to identify soybean pods present in the plant:
   <p align="justify">
        It is possible to identify that at the moment our Artificial Intelligence is not able to recognize all the pods present in the plant, demonstrating that the model still needs improvements that will be implemented in the next Sprints 
  </p>

 | *Plants*   | *Resutls* | 
 | ---------- | --------- |
 | <img src="https://github.com/medrenan/SoyIA/blob/main/doc/Imagens/Results%20IA/Results%20IA%20Sprint%202/Resultado%20Soja-1.png" height="250"> | <p align="justify"> In this image we have 20 pods and 60 seeds, the AI ​​identified exactly 17 plants and 46 seeds </p> |
 | <img src="https://github.com/medrenan/SoyIA/blob/main/doc/Imagens/Results%20IA/Results%20IA%20Sprint%202/Resultado%20Soja-2.png" height="330"> | <p align="justify"> In this image we have 26 pods and 75 seeds, the AI ​​identified exactly 23 pods and 62 seeds </p> |
 | <img src="https://github.com/medrenan/SoyIA/blob/main/doc/Imagens/Results%20IA/Results%20IA%20Sprint%202/Resultado%20Soja-3.png" height="400"> | <p align="Justify"> In this image we have 18 pods and 54 seeds, the AI ​​identified exactly 18 plants and 48 seeds </p> |
 
<p align="justify"> 
        - Considering a sample of 10 test images the AI ​​identified 82.5% of the total pods of the 10 images and through an estimate of 2.6 grains per pod identified 96.42% of the total grains. This number ended up being greater than the number of pods as was estimated, in some cases it calculated more grains than there were in the plant which ended up compensating in the images she identified less.
        </p>
        
  <p align="justify">
  - The average confidence the AI ​​had for each pod it scored was 55.62% (is the confidence if what she marked is in fact a pod and this number is generated
automatically by AI).
  
  </p>
        
 
# Delivery Schedule 🗓

 
| *Sprints*  | *About* | *Delivery*    | *README*  | *Release* |
| ---------- | ------  | ------------- | ------    | --------- |
|  Sprint 1  | AI modeling and training to identify soybean pods present in plant photos. | 18/09 | [View](https://github.com/medrenan/SoyIA/edit/main/doc/README/README%20Sprint1.md) | [Download](https://github.com/medrenan/SoyIA/releases/tag/sprint1) |
|  Sprint 2  | Implement and train image recognition and classification AI for seed count in soybean pods.  | 09/10 | [View](https://github.com/medrenan/SoyIA/blob/main/doc/README/README%20Sprint2.md) | [Download](#)|
|  Sprint 3  | Implementing AI in the application with user core functionalities. | 06/11 | [-](#) | [-](#) |
|  Sprint 4  | Improved effectiveness of seed identification and user functionality. | 27/11 | [-](#) | [-](#) |     

# Team 👩‍💻👨‍💻

<body>
        <div align="center">
                <table>
                <thead>
                        <th>Scrum Master</th>
                        <th>Product Owner</th>
                        <th>Dev Team</th>
                        <th>Dev Team</th>
                        <th>Dev Team</th>
                        <th>Dev Team</th>
                        <th>Dev Team</th>
                        <th>Dev Team</th>
                <thead>
                <tbody>
                        <tr>
                                <th><a href="https://github.com/medrenan"><img src="https://avatars.githubusercontent.com/u/64873343?v=4"" width="75px" height="75px"/></a></th>
                                <th><a href="https://github.com/nicursino"><img src="https://avatars.githubusercontent.com/u/67070670?s=64&v=4" width="75px" height="75px"/></a></th>
                                <th><a href="https://github.com/CarolinaMargiotti"><img src="https://avatars.githubusercontent.com/u/55335180?s=64&v=4" width="75px" height="75px"/></a></th>
                                <th><a href="https://github.com/CristianMateusTB"><img src="https://avatars.githubusercontent.com/u/67056255?s=64&v=4" width="75px" height="75px"/></a></th>
                                <th><a href="https://github.com/DanVargaa"><img src="https://avatars.githubusercontent.com/u/60754290?s=64&v=4" width="75px" height="75px"/></a></th>
                                <th><a href="https://github.com/Ffelipe-Ssilva"><img src="https://avatars.githubusercontent.com/u/65372142?s=64&v=4" width="75px" height="75px"/></a></th>
                                <th><a href="https://github.com/Rafael-BD"><img src="https://avatars.githubusercontent.com/u/67149165?s=64&v=4" width="75px" height="75px"/></a></th>
                                <th><a href="https://github.com/rafaeldossper"><img src="https://avatars.githubusercontent.com/u/68171764?s=64&v=4" width="75px" height="75px"/></a></th>
                        </tr>
                        <tr>
                                <th><a href="https://www.linkedin.com/in/medrenan/""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></th>
                                <th><a href="https://www.linkedin.com/in/nicolas-cursino-406935184/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></th>
                                <th><a href="https://www.linkedin.com/in/carolina-margiotti-703897193/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></th>
                                <th><a href="https://www.linkedin.com/mwlite/in/cristian-mateus-2960ab1ab"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></th>
                                <th><a href="https://www.linkedin.com/in/daniel-vargas-8b806a184"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></th>
                                <th><a href=""><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></th>
                                <th><a href="https://www.linkedin.com/in/rafael-b-990835209"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></th>
                                <th><a href="linkedin.com/in/rafaeldossper"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a></th>
                        </tr>
                <tbody>
        </table>
        </div>
</body>
