import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { MatDialogRef } from '@angular/material/dialog';
import { Item } from 'src/app/models/item.model';
import { City, State } from 'src/app/models/state.model';
import { ItemsApiService } from 'src/app/services/items-api.service';
import { StatesApiService } from 'src/app/services/states-api.service';

@Component({
  selector: 'app-edit-add-item-dialog',
  templateUrl: './edit-add-item-dialog.component.html',
  styleUrls: ['./edit-add-item-dialog.component.scss'],
})
export class EditAddItemDialogComponent implements OnInit {
  itemDescription = '';
  itemModelNumber = '';
  itemManufacturer = '';
  itemCity = new FormControl('');
  itemName = new FormControl('', [
    Validators.required,
    Validators.minLength(2),
  ]);
  itemPurchasedPrice = new FormControl('');
  itemSku = new FormControl('');
  itemState!: State;
  states: State[] = [];
  categories: any = [];
  itemCategory = '';

  constructor(
    public dialogRef: MatDialogRef<EditAddItemDialogComponent>,
    private itemsApiService: ItemsApiService,
    private statesApiService: StatesApiService
  ) {}

  ngOnInit(): void {
    this.loadStates();
    this.loadCategories();
  }

  loadStates() {
    this.statesApiService.listStates().subscribe((value) => {
      this.states = value;
    });
  }

  loadCategories() {
    this.itemsApiService.listCategories().subscribe((value) => {
      this.categories = value;
    });
  }

  onNoClick(): void {
    this.dialogRef.close();
  }

  saveItem() {
    const city: City = {
      name: this.itemCity.value
    };
    const item: Item = {
      category: "Music",
      city: city,
      description: this.itemDescription,
      manufacturer: this.itemManufacturer,
      model_number: this.itemModelNumber,
      name: this.itemName.value,
      purchased_price: this.itemPurchasedPrice.value,
      sku: this.itemSku.value,
      state: this.itemState,
    };
    this.itemsApiService.createItem(JSON.stringify(item)).subscribe(() => {
      this.dialogRef.close();
    });
  }
}
