import { Injectable } from '@angular/core';
import {
  HttpClient,
  HttpErrorResponse,
  HttpHeaders,
} from '@angular/common/http';
import { API_URL } from '../env';
import { State } from '../models/state.model';

@Injectable()
export class StatesApiService {
  constructor(private http: HttpClient) {}

  httpHeader = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    }),
  };

  private _handleError(err: HttpErrorResponse | any) {
    return err.message || 'Error: Unable to complete request.';
  }

  listStates() {
    return this.http.get<State[]>(`${API_URL}/states`);
  }
}
