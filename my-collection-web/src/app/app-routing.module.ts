import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { ItemDetailComponent } from './pages/item-detail/item-detail.component';
import { ItemsComponent } from './pages/items/items.component';

const routes: Routes = [
  {
    path: '',
    component: AppComponent,
  },
  {
    path: 'items',
    component: ItemsComponent,
    // canActivate: [CanActivateRouteService]
  },
  {
    path: 'item/:id',
    component: ItemDetailComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
