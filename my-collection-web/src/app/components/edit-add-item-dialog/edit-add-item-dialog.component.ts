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
  itemCity = new FormControl('');
  itemName = new FormControl('', [
    Validators.required,
    Validators.minLength(2),
  ]);
  itemPurchasedPrice = new FormControl('');
  itemSku = new FormControl('');
  itemState = new FormControl('');
  states: State[] = [];

  constructor(
    public dialogRef: MatDialogRef<EditAddItemDialogComponent>,
    private itemsApiService: ItemsApiService,
    private statesApiService: StatesApiService
  ) {}

  ngOnInit(): void {
    this.loadStates();
  }

  loadStates() {
    this.statesApiService.listStates().subscribe((value) => {
      this.states = value;
    });
  }

  onNoClick(): void {
    this.dialogRef.close();
  }

  saveItem() {
    const state: State = {
      name: 'Texas',
      abrv: 'TX',
    };
    const city: City = {
      name: 'Austin'
    };
    const item: Item = {
      name: this.itemName.value,
      purchased_price: this.itemPurchasedPrice.value,
      sku: this.itemSku.value,
      city: city,
      description: this.itemDescription,
      state: state,
    };
    this.itemsApiService.createItem(JSON.stringify(item)).subscribe(() => {
      this.dialogRef.close();
    });
  }
}
