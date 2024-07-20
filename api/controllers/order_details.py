from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas
def create(db: Session, OrderDetail: schemas.OrderDetail):
    # Create a new instance of the OrderDetail model with the provided data
    db_OrderDetail = models.OrderDetail(
        name=OrderDetail.name,
        description=OrderDetail.description
    )
    # Add the OrderDetail to the database session
    db.add(db_OrderDetail)
    # Commit the changes to the database
    db.commit()
    # Refresh the OrderDetail object to ensure it reflects the current state in the database
    db.refresh(db_OrderDetail)
    # Return the newly created OrderDetail object
    return db_OrderDetail


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, OrderDetail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == OrderDetail_id).first()


def update(db: Session, OrderDetail_id: int, OrderDetail: schemas.OrderDetailUpdate):
    # Query the database for the specific OrderDetail to update
    db_OrderDetail = db.query(models.OrderDetail).filter(models.OrderDetail.id == OrderDetail_id)
    # Extract the update data from the provided 'OrderDetail' object
    update_data = OrderDetail.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_OrderDetail.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated OrderDetail record
    return db_OrderDetail.first()


def delete(db: Session, OrderDetail_id: int):
    # Query the database for the specific OrderDetail to delete
    db_OrderDetail = db.query(models.OrderDetail).filter(models.OrderDetail.id == OrderDetail_id)
    # Delete the database record without synchronizing the session
    db_OrderDetail.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
