import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { MatDialogRef } from '@angular/material/dialog';
import { Item } from 'src/app/models/item.model';
import { ItemsApiService } from 'src/app/services/items-api.service';

@Component({
  selector: 'app-edit-add-item-dialog',
  templateUrl: './edit-add-item-dialog.component.html',
  styleUrls: ['./edit-add-item-dialog.component.scss'],
})
export class EditAddItemDialogComponent implements OnInit {
  itemName = new FormControl('', [
    Validators.required,
    Validators.minLength(2),
  ]);
  itemPurchasedPrice = new FormControl('');
  itemSku = new FormControl('');
  itemLocation = new FormControl('');
  itemDescription = '';

  constructor(
    public dialogRef: MatDialogRef<EditAddItemDialogComponent>,
    private itemsApiService: ItemsApiService
  ) {}

  ngOnInit(): void {}

  onNoClick(): void {
    this.dialogRef.close();
  }

  saveItem() {
    const item: Item = {
      name: this.itemName.value,
      purchased_price: this.itemPurchasedPrice.value,
      sku: this.itemSku.value,
      location: this.itemLocation.value,
      description: this.itemDescription,
    };
    this.itemsApiService.createItem(JSON.stringify(item)).subscribe(() => {
      this.dialogRef.close();
    });
  }
}
