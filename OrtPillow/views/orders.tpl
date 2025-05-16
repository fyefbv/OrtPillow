% rebase('layout.tpl', title='Orders', year=year)

<div class="container body-content">
    <h2 class="section-title">Order Management</h2>

    <!-- Add New Order Form -->
    <div class="marketplace-card">
        <form action="/orders" method="post" class="message-form">
            <div class="form-group">
                <input type="number" name="order_id" class="form-input"
                       placeholder="Order ID" value="{{order_id}}">
                % if order_id_error:
                <span class="field-validation-error">{{order_id_error}}</span>
                % end
            </div>

            <div class="form-group">
                <input type="text" name="product" class="form-input"
                       placeholder="Product Name" value="{{product}}">
                % if product_error:
                <span class="field-validation-error">{{product_error}}</span>
                % end
            </div>

            <div class="form-group">
                <input type="date" name="date" class="form-input"
                       placeholder="Date" value="{{date}}">
                % if date_error:
                <span class="field-validation-error">{{date_error}}</span>
                % end
            </div>

            <div class="form-group">
                <input type="tel" name="phone" class="form-input"
                       placeholder="Phone (+7XXXXXXXXXX)"
                       pattern="\+7\d{10}"
                       value="{{phone}}">
                % if phone_error:
                <span class="field-validation-error">{{phone_error}}</span>
                % end
            </div>

            <button type="submit" class="btn-marketplace">Add Order</button>
        </form>
    </div>

    <!-- Orders List -->
    <div class="stats-grid" style="margin-top: 40px;">
        % for order in sorted_orders:
        <div class="stat-card">
            <div class="stat-number">#{{order['order_id']}}</div>
            <div class="stat-label">{{order['product']}}</div>
            <div class="text-primary" style="margin-top: 10px;">
                {{order['date']}}<br>
                {{order['phone']}}
            </div>
        </div>
        % end
    </div>
</div>