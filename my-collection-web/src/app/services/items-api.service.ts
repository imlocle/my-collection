import { Injectable } from '@angular/core';
import {
  HttpClient,
  HttpErrorResponse,
  HttpHeaders,
} from '@angular/common/http';
import { API_URL } from '../env';
import { Item } from '../models/item.model';
import { catchError, Observable } from 'rxjs';

@Injectable()
export class ItemsApiService {
  constructor(private http: HttpClient) {}
  httpHeader = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    }),
  };

  private _handleError(err: HttpErrorResponse | any) {
    return err.message || 'Error: Unable to complete request.';
  }

  listItems() {
    return this.http.get<Item[]>(`${API_URL}/items`);
  }

  createItem(item: string): Observable<any> {
    console.log(item);
    return this.http
      .post(`${API_URL}/item`, item, this.httpHeader)
      .pipe(
        catchError(this._handleError(`Error: Failed to create item: ${item}`))
      );
  }

  getItem(id: number) {
    return this.http
      .get<Item>(`${API_URL}/item/${id}`)
      .pipe(catchError(this._handleError(`Error: Failed to get item: ${id}`)));
  }

  deleteItem(id: number): Observable<undefined> {
    return this.http
      .delete(`${API_URL}/item/${id}`, this.httpHeader)
      .pipe(
        catchError(this._handleError(`Error: Failed to delete item: ${id}`))
      );
  }
}
