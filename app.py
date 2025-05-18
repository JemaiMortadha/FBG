from flask import Flask, request, jsonify
from models import db, User, Product, Feedback

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"id": new_user.id, "name": new_user.name}), 201

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], description=data.get('description'))
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"id": new_product.id, "name": new_product.name}), 201

@app.route('/feedback', methods=['POST'])
def add_feedback():
    data = request.get_json()
    new_feedback = Feedback(
        user_id=data['user_id'],
        product_id=data['product_id'],
        rating=data['rating'],
        comment=data.get('comment')
    )
    db.session.add(new_feedback)
    db.session.commit()
    return jsonify({
        "id": new_feedback.id,
        "user_id": new_feedback.user_id,
        "product_id": new_feedback.product_id,
        "rating": new_feedback.rating,
        "comment": new_feedback.comment,
        "date": new_feedback.date.isoformat()
    }), 201

@app.route('/feedback', methods=['GET'])
def get_all_feedback():
    feedbacks = Feedback.query.all()
    result = [{
        "id": f.id,
        "user_id": f.user_id,
        "product_id": f.product_id,
        "rating": f.rating,
        "comment": f.comment,
        "date": f.date.isoformat()
    } for f in feedbacks]
    return jsonify(result)

@app.route('/products/<int:product_id>/feedback', methods=['GET'])
def get_feedback_by_product(product_id):
    feedbacks = Feedback.query.filter_by(product_id=product_id).all()
    result = [{
        "id": f.id,
        "user_id": f.user_id,
        "rating": f.rating,
        "comment": f.comment,
        "date": f.date.isoformat()
    } for f in feedbacks]
    return jsonify(result)

@app.route('/users/<int:user_id>/feedback', methods=['GET'])
def get_feedback_by_user(user_id):
    feedbacks = Feedback.query.filter_by(user_id=user_id).all()
    result = [{
        "id": f.id,
        "product_id": f.product_id,
        "rating": f.rating,
        "comment": f.comment,
        "date": f.date.isoformat()
    } for f in feedbacks]
    return jsonify(result)

@app.route('/feedback/<int:id>', methods=['DELETE'])
def delete_feedback(id):
    feedback = Feedback.query.get_or_404(id)
    db.session.delete(feedback)
    db.session.commit()
    return jsonify({"message": "Feedback deleted"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
