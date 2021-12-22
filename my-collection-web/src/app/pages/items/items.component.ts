import { Component, OnInit, ViewChild } from '@angular/core';
import { Item } from '../../models/item.model';
import { ItemsApiService } from '../../services/items-api.service';
import { MatTableDataSource } from '@angular/material/table';
import { MatSort } from '@angular/material/sort';
import { Observable } from 'rxjs';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { EditAddItemDialogComponent } from 'src/app/components/edit-add-item-dialog/edit-add-item-dialog.component';
import { FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'items',
  templateUrl: './items.component.html',
  styleUrls: ['./items.component.scss'],
})
export class ItemsComponent implements OnInit {
  displayedColumns: string[] = [
    'name',
    'purchased_price',
    'location',
    'description',
    'sku',
    'remove',
  ];
  dataSource!: Observable<Item[]>;

  constructor(
    private itemsApiService: ItemsApiService,
    public dialog: MatDialog
  ) {}

  ngOnInit(): void {
    this.loadItems();
  }

  loadItems() {
    const items = this.itemsApiService.listItems();
    this.dataSource = this.itemsApiService.listItems();
  }

  addItem() {
    const dialogRef = this.dialog.open(EditAddItemDialogComponent, {
      width: '700px',
    });

    dialogRef.afterClosed().subscribe(() => {
      console.log('Edit Add Item Dialog closed.');
      this.loadItems();
    });
  }

  removeItem(id: number) {
    this.itemsApiService.deleteItem(id).subscribe(() => {
      console.log(`Item: ${id}: Deleted`);
      this.loadItems();
    });
  }
}
