export class Item {
  constructor(
    public name: string,
    public purchased_price: number,
    public sku?: string,
    public location?: string,
    public description?: string,
    public _id?: number,
    public updatedAt?: Date,
    public createdAt?: Date,
    public lastUpdatedBy?: string
  ) {}
}
