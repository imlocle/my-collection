import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { Item } from './models/item.model';
import { ItemsApiService } from './services/items-api.service';
import { ItemsComponent } from './pages/items/items.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {}
