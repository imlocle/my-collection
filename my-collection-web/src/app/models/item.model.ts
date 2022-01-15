import { State, City } from './state.model';

export class Item {
  constructor(
    public name: string,
    public purchased_price: number,
    public state?: State,
    public sku?: string,
    public city?: City,
    public description?: string,
    public _id?: number,
    public updatedAt?: Date,
    public createdAt?: Date,
    public lastUpdatedBy?: string
  ) {}
}
