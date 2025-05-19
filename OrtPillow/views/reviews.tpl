% rebase('layout.tpl', title='Orders', year=year)

<div class="container body-content">
    <h2 class="section-title">Leave Your Review</h2>

    <div class="review-form-container">
        <form action="/reviews" method="post" class="review-form">
            <p><input type="text" name="author" class="form-control" 
                    placeholder="Your Name" value="{{author}}">
                % if errors.get('author'):
                    <span class="text-danger">{{errors['author']}}</span>
                % end
            </p>

            <p><input type="tel" name="phone" class="form-control"
                    placeholder="Phone +7 (xxx) xxx-xx-xx"
                    value="{{phone}}">
                % if errors.get('phone'):
                    <span class="text-danger">{{errors['phone']}}</span>
                % end
            </p>

            <div class="form-group">
                <p><textarea name="text" class="form-control wide-textarea" 
                        placeholder="Your Review" rows="7">{{text}}</textarea>
                % if errors.get('text'):
                    <span class="text-danger">{{errors['text']}}</span>
                % end
                </p>
            </div>

            <button type="submit" class="submit-button">Submit Review</button>
        </form>
    </div>

    % for review in sorted_reviews:
        <div class="review-item">
            <div class="review-header">
                <div class="author-info">
                    <span class="author">{{review['author']}}</span>
                    <span class="phone-separator">/</span>
                    <span class="phone">{{review['phone']}}</span>
                </div>
                <span class="date">{{review['date']}}</span>
            </div>
            <div>
                <div class="review-text-wrapper">
                    <p class="review-text">{{review['text']}}</p>
                </div>
            </div>
        </div>
    % end
</div>