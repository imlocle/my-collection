import { Component, OnInit } from '@angular/core';
import { Item } from 'src/app/models/item.model';
import { ItemsApiService } from 'src/app/services/items-api.service';

@Component({
  selector: 'item-detail',
  templateUrl: './item-detail.component.html',
  styleUrls: ['./item-detail.component.scss']
})
export class ItemDetailComponent implements OnInit {
  dataSource!: Item;
  constructor(private itemsApiService: ItemsApiService) { }

  ngOnInit(): void {

  }

  getItemDetail(id: number) {
    this.itemsApiService.getItem(id).subscribe((value) => {
      this.dataSource = value;
    })
  }
}
