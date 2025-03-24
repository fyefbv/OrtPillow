<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - My Bottle Application</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body style="background-color: #ffffff;"> <!-- Основной белый фон -->
    <div class="navbar navbar-inverse navbar-fixed-top" style="background-color: #007b7b; border-color: #006666;">
        <div class="container">
            <div class="navbar-header" style="height: 40px;">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar" style="background-color: #ffffff;"></span>
                    <span class="icon-bar" style="background-color: #ffffff;"></span>
                    <span class="icon-bar" style="background-color: #ffffff;"></span>
                </button>
                <a href="/" class="navbar-brand" style="color: #ffffff;">
                    <img src="/static/images/ort_pillow_logo.png" alt="Logo" style="height: 30px;">
                </a>
            </div>
            <div class="navbar-collapse collapse" style="padding-top: 5px; padding-bottom: 5px;">
                <ul class="nav navbar-nav">
                    <li><a href="/home" style="color: #ffffff;">Home</a></li>
                    <li><a href="/about" style="color: #ffffff;">About</a></li>
                    <li><a href="/contact" style="color: #ffffff;">Contact</a></li>
                </ul>
            </div>
        </div>
    </div>

    <div class="container body-content">
        {{!base}}
        <hr />
        <footer style="color: #666666; text-align: center; padding: 15px;">
            <p>&copy; {{ year }} - OrtPillow Company</p>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
