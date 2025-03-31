% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron">
    <h1>Ort Pillow</h1>
    <p class="lead">Ort Pillow - the best online store for orthopedic pillows</p>
    <p><a href="https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B4%D1%83%D1%88%D0%BA%D0%B0" class="btn btn-primary btn-large">Learn more &raquo;</a>
</div>

<div class="container">
    <div class="row justify-content-center">
        % for product in products:
        <div class="col-md-4 mb-4">
            <div class="card h-100">
                <div class="card-img-container">
                    <img src="{{ product['image'] }}" class="card-img-top" alt="{{ product['name'] }}">
                </div>
                <div class="card-body">
                    <h5 class="card-title">{{ product['name'] }}</h5>
                    <p class="card-text">{{ product['description'] }}</p>
                    <div class="d-flex justify-content-between align-items-center">
                        <h4 class="text-primary">{{ product['price'] }}</h4>
                        <a href="https://www.ozon.ru/product/ortopedicheskaya-podushka-pappus-two-correct-53-38-sm-vysota-12-14-sm-pod-navolochku-50-440980327/?at=mqtkyW9kqh4N2KGMc8zVXy6hKNlV7Gu4pZnBzcAgkRwL&keywords=%D0%BE%D1%80%D1%82%D0%BE%D0%BF%D0%B5%D0%B4%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5+%D0%BF%D0%BE%D0%B4%D1%83%D1%88%D0%BA%D0%B8" 
                        class="btn btn-success">Buy Now</a>
                    </div>
                </div>
            </div>
        </div>
        % end
    </div>
</div>

<div class="container mt-5">
    <div class="row">
        <div class="col-12">
            <h3 class="text-center mb-4">Also available on:</h3>
        </div>
    </div>
    <div class="row marketplace-row">
        <div class="col-md-4 mb-4">
            <div class="marketplace-card">
                <h2>Ozon</h2>
                <p>Our pillows on Ozon</p>
                <a class="btn btn-marketplace" href="https://www.ozon.ru/">Learn more &raquo;</a>
            </div>
        </div>
        <div class="col-md-4 mb-4">
            <div class="marketplace-card">
                <h2>Wildberries</h2>
                <p>Our pillows on Wildberries</p>
                <a class="btn btn-marketplace" href="https://www.wildberries.ru/">Learn more &raquo;</a>
            </div>
        </div>
        <div class="col-md-4 mb-4">
            <div class="marketplace-card">
                <h2>Amazon</h2>
                <p>Our pillows on Amazon</p>
                <a class="btn btn-marketplace" href="https://www.amazon.com/">Learn more &raquo;</a>
            </div>
        </div>
    </div>
</div>
