<!DOCTYPE html>
<html lang="en">
   <head>
      <title>{{ title }}</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
   </head>

   <body>
     <center>
      <br>
      <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Goethe_University_logo.jpg" height="104" width="220">
      <h1> Welcome to BigBench2</h1>
      <h2> Last update: {{ time }}</h2>
      <br>

<button class="btn btn-primary"  onclick="self.location.href='http://127.0.0.1:5000/activateScripts'"
>Activate scripts</button>

<button class="btn btn-primary"  onclick="self.location.href='http://127.0.0.1:5000/checkPreRequirements'"
>Check pre-requirements</button>

<button class="btn btn-primary"  onclick="self.location.href='http://127.0.0.1:5000/prepStartSpark'"
>Prep-start-spark</button>

<button class="btn btn-primary"  onclick="self.location.href='http://127.0.0.1:5000/startMinikube'"
>Start minikube</button>

<button class="btn btn-primary"  onclick="self.location.href='http://127.0.0.1:5000/activateScripts'"
>Minikube dashboard</button>

<button class="btn btn-primary"  onclick="self.location.href='http://127.0.0.1:5000/minikubeDashboard'"
>Minikube Dashboard</button>

<button class="btn btn-primary"  onclick="self.location.href='http://127.0.0.1:5000/stopMinikube'"
>Minikube stop</button>

<br>
<!-- other style button
<input type="button" name="lien2" value="Stop minikube"
onclick="self.location.href='http://127.0.0.1:5000/stopMinikube'"
style="background-color:#668fff"
style="color:white; font-weight:bold"onclick> -->
<body>
<div id="allButFooter">

<footer id="footnotes" class="col-sm-9" style="position: fixed; bottom: 0; width: 100%;">
Copyright © 2019
<strong class="master">Master Thesis Project</strong>
<strong class="spacer"> | </strong>
<strong class="Name">Vasil Radushev</strong>
<strong class="spacer"> | </strong>
<strong class="uni">Goethe University Frankfurt</strong>
<br>
<small>GitLab: <a href="https://gitlab.com/o7ka4aln1ka/bigbench2_master/">BigBench2</a>.</small>
</footer>
</div>
</body>

    </center>
   </body>
</html>
